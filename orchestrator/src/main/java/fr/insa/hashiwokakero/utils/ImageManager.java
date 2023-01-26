package fr.insa.hashiwokakero.utils;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

import org.springframework.core.io.InputStreamResource;
import org.springframework.web.multipart.MultipartFile;

public class ImageManager {
    public static void saveImage(MultipartFile file, String filename, String path) throws IOException{
        Path uploadPath = Paths.get(path);
         
        try (InputStream inputStream = file.getInputStream()) {
            Path filePath = uploadPath.resolve(filename);
            Files.copy(inputStream, filePath, StandardCopyOption.REPLACE_EXISTING);
        } catch (IOException ioe) {        
            ioe.printStackTrace();
            throw new IOException("Could not save image file: " + filename, ioe);
        }      
    }

    public static InputStreamResource getImage(String filename, String path) throws IOException{
        File file = new File(path+'/'+filename);
        InputStreamResource resource = new InputStreamResource(new FileInputStream(file));
        return resource;
    }

    public static void saveByteImage(byte[] image, String filename, String path) {

        FileOutputStream fos = null;
        try {
            fos = new FileOutputStream(new File(path+filename));
            fos.write(image);
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (fos != null) {
                    fos.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        
    }

}
