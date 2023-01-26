package fr.insa.hashiwokakero.service;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import fr.insa.hashiwokakero.utils.SSHClient;


@Service
public class ManagerService {
    @Value("${upload.dir}")
    private String uploadDir;

    @Value("${solved.dir}")
    private String resultDir;
    
    public byte[] deleteOriginalImages() throws IOException {
        return deleteFiles(uploadDir);
    }

    public byte[] deleteSolvedImages() throws IOException {
        return deleteFiles(resultDir);
    }

    private byte[] deleteFiles(String path) throws IOException {
        byte[] buffer = new byte[1024];
        byte[] zip = new byte[0];
        
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ZipOutputStream zos = new ZipOutputStream(baos);
        File dir = new File(path);
        File[] files = dir.listFiles();
        if (files != null) { 
            for (File file : files) {
                if (file.isFile()) {
                    FileInputStream fis = new FileInputStream(file);
                    zos.putNextEntry(new ZipEntry(file.getName()));
                    int length;
                    while ((length = fis.read(buffer)) > 0) {
                        zos.write(buffer, 0, length);
                    }
                    zos.closeEntry();
                    fis.close();
                }
            }
            zos.close();
            zip = baos.toByteArray();
         
            for (File file : files) {
                if (file.isFile()) {
                    file.delete();
                }
            }
        }
        return zip;
    }

    public void launchGridSolvingService() throws Exception {
        SSHClient.listFolderStructure("user", "user", "7.0.0.241", 22, "python3.7 /home/user/Documents/sol1/grid-solving/code/app.py &");
    }

    public void launchImageRecognitionService() {
    }

    public void launchImageCreationService() throws Exception {
        SSHClient.listFolderStructure("user", "user", "7.0.0.216", 22, "cd /home/user/Documents/image-creation/utils/; python3.9 app.py &");
    }
}
