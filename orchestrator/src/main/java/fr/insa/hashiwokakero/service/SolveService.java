package fr.insa.hashiwokakero.service;

import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.List;
import java.util.UUID;

import javax.print.attribute.standard.Sides;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.InputStreamResource;
import org.springframework.core.task.TaskExecutor;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import fr.insa.hashiwokakero.client.GridProbSolvingClient;
import fr.insa.hashiwokakero.client.ImageCreationClient;
import fr.insa.hashiwokakero.client.ImageRecognitionClient;
import fr.insa.hashiwokakero.modele.solving.GridProb;
import fr.insa.hashiwokakero.modele.solving.SolvedGridNode;
import fr.insa.hashiwokakero.utils.ImageManager;

@Service
public class SolveService {

	@Value("${upload.dir}")
	private String uploadDir;

	@Value("${solved.dir}")
	private String resultDir;


	@Value("${image.extension}")
	private String imageExtension;


	@Autowired
	private TaskExecutor taskExecutor;

	@Autowired
	private ImageRecognitionClient imageRecognitionClient;

	@Autowired
	private GridProbSolvingClient gridProbSolvingClient;

	@Autowired
	private ImageCreationClient imageCreationClient;

	
	
	HashMap<String, Integer> solvingStatus = new HashMap<String, Integer>();

	class SolvingRunner implements Runnable {


		private String uuid;
		private SolveService solveService;
		private int size;
		

		public SolvingRunner(SolveService solveService, String uuid, int size) {
			this.solveService = solveService;
			this.uuid = uuid;
			this.size = size;
		}

		@Override
		public void run() {
			System.out.println("LOG - solving started : "+uuid);
			solveService.solvingStatus.put(uuid, 0);
			byte[] image=null;
			try {
				 InputStream is = ImageManager.getImage(uuid+imageExtension, uploadDir).getInputStream();
				 image = is.readAllBytes();
				 is.close();
			} catch (IOException e) {
				e.printStackTrace();
				return;
			}
			GridProb grid=null;
			try{
				grid = imageRecognitionClient.recognize(image,size);
			}catch(Exception e) {
				System.out.println("LOG - Image recognition failed : "+uuid);
				solveService.solvingStatus.put(uuid, -1);
				return;
			}
			
			System.out.println("LOG - Image recognition achieved: "+uuid);
			System.out.println("Grid : "+grid);
			solveService.solvingStatus.put(uuid, 1);

			List<List<SolvedGridNode>> solvedGrid = null;
			try{
				solvedGrid = gridProbSolvingClient.solve(grid);
			}catch(Exception e) {
				System.out.println("LOG - Grid solving failed : "+uuid);
				solveService.solvingStatus.put(uuid, -1);
				return;
			}
			System.out.println("LOG - Grid solving achieved: "+uuid);
			System.out.println("Solved grid : "+solvedGrid);
			solveService.solvingStatus.put(uuid, 2);

			
			byte[] solvedImage = null;
			try{
				solvedImage = imageCreationClient.createImage(solvedGrid);
			}catch(Exception e) {
				System.out.println("LOG - Image creation failed : "+uuid);
				solveService.solvingStatus.put(uuid, -1);
				return;
			}
			System.out.println("LOG - Image creation achieved: "+uuid);
			solveService.solvingStatus.put(uuid, 3);
			
			ImageManager.saveByteImage(solvedImage, uuid+imageExtension, resultDir);
			System.out.println("LOG - Image saved : "+uuid);
			solveService.solvingStatus.put(uuid, 4);
			return;
		}
		
	}

    public String launchSolving(MultipartFile file, int size) throws IOException{
		
		String uuid = UUID.randomUUID().toString(); 
        ImageManager.saveImage(file, uuid+imageExtension, uploadDir);
        System.out.println("LOG - Image uploaded : "+uuid+" ("+file.getOriginalFilename()+")");
		taskExecutor.execute(new SolvingRunner(this, uuid,size));
		return uuid;
    }
	
	public Integer getSolvingStatus(String uuid) {
		return solvingStatus.get(uuid);
	}

	public ResponseEntity<InputStreamResource> getResultImage(String uuid) {
        InputStreamResource resource;
        try {
            resource = ImageManager.getImage(uuid+imageExtension, resultDir);
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND)
                    .body(null);
        }

        return ResponseEntity.ok()
                .contentType(MediaType.IMAGE_JPEG)
                .body(resource);
	}

}
