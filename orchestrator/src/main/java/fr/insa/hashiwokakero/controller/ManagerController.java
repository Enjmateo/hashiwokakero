package fr.insa.hashiwokakero.controller;

import java.io.IOException;

import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ContentDisposition;
import org.springframework.http.HttpHeaders;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.RestController;

import fr.insa.hashiwokakero.service.ManagerService;
import org.springframework.web.bind.annotation.PostMapping;


@RestController
public class ManagerController {

    @Autowired
    private ManagerService managerService;
    
    @DeleteMapping(path = "images/original", produces = "application/octet-stream")
    public byte[] deleteOriginal(HttpServletResponse response) throws IOException {
        final ContentDisposition contentDisposition = ContentDisposition.builder("attachment")
                .filename("original-pictures.zip").build();
        response.setHeader(HttpHeaders.CONTENT_DISPOSITION, contentDisposition.toString());
        return managerService.deleteOriginalImages();
    }

    @DeleteMapping(path = "images/solved", produces = "application/octet-stream")
    public byte[] deleteSolved(HttpServletResponse response) throws IOException {
        final ContentDisposition contentDisposition = ContentDisposition.builder("attachment")
                .filename("solved-pictures.zip").build();
        response.setHeader(HttpHeaders.CONTENT_DISPOSITION, contentDisposition.toString());
        return managerService.deleteSolvedImages();
    }

    @PostMapping("/launch/grid-solving-service")
    public void launchGridSolvingService() throws Exception {
        managerService.launchGridSolvingService();
    }

    @PostMapping("/launch/image-recognition-service")
    public void launchImageRecognitionService() {
        managerService.launchImageRecognitionService();
    }

    @PostMapping("/launch/image-creation-service")
    public void launchImageCreationService() throws Exception {
        managerService.launchImageCreationService();
    }
    
    
}
