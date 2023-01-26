package fr.insa.hashiwokakero.controller;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import fr.insa.hashiwokakero.client.GridProbSolvingClient;
import fr.insa.hashiwokakero.client.GridSolvingClient;
import fr.insa.hashiwokakero.client.ImageCreationClient;
import fr.insa.hashiwokakero.modele.solving.Grid;
import fr.insa.hashiwokakero.modele.solving.GridProb;
import fr.insa.hashiwokakero.modele.solving.SolvedGridNode;
import fr.insa.hashiwokakero.utils.ImageManager;
import io.swagger.v3.oas.annotations.media.Schema;

@RestController
public class TestController {
    
    @Autowired
	private GridSolvingClient gridSolvingClient;

    @Autowired
    private GridProbSolvingClient gridProbSolvingClient;

    @Autowired
    private ImageCreationClient imageCreationClient;
    
    @PostMapping(path="/test-solver", produces = "image/jpeg"   )
    public byte[] testSolving(
        @Schema(example = "[[4,0,3,0], [0,0,1,0], [0,0,0,0], [2,0,0,0]]")
        @RequestBody Integer[][] rawGrid) throws Exception{
        Grid grid  = new Grid(rawGrid.length,rawGrid);
		System.out.println(grid);
		List<List<SolvedGridNode>> solvedGrid = this.gridSolvingClient.solve(grid);
		System.out.println(solvedGrid);
        byte[] image = this.imageCreationClient.createImage(solvedGrid);
        ImageManager.saveByteImage(image,"result-test.solved.jpeg","files/");
        return image;
    }

    @PostMapping(path="/test-solver-prob", produces = "image/jpeg"   )
    public byte[] testSolvingProb(
        @Schema(example = "[[[0, 25, 0, 10, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [75, 25, 0, 10, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]], [[0, 25, 55, 10, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 45, 0, 10, 0, 14, 0, 0]]]")
        @RequestBody Integer[][][] rawGrid) throws Exception{
        GridProb grid  = new GridProb(rawGrid.length,rawGrid);
		System.out.println(grid);
		List<List<SolvedGridNode>> solvedGrid = this.gridProbSolvingClient.solve(grid);
		System.out.println(solvedGrid);
        byte[] image = this.imageCreationClient.createImage(solvedGrid);
        ImageManager.saveByteImage(image,"result-test.solved-prob.jpeg","files/");
        return image;
    }

    @PostMapping("/recognize")
    public void recognize(@RequestBody byte[] file) throws Exception{
        System.out.println("LOG - recognize : "+file);
        Path uploadPath = Paths.get("files");
        Path filePath = uploadPath.resolve("test-recognize-call.jpeg");
        Files.write(filePath, file);
    }
}
