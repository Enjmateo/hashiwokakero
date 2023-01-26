package fr.insa.hashiwokakero.controller;

import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.InputStreamResource;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import fr.insa.hashiwokakero.service.SolveService;


@RestController
public class SolveController {

    @Autowired
    private SolveService solveService;

    @PostMapping(path="/solving/upload-image", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
    public ResponseEntity<String> uplaodImage(@RequestParam("image") MultipartFile file, @RequestParam("size") int size)
            throws IOException {
        return ResponseEntity.status(HttpStatus.OK)
                .body(solveService.launchSolving(file,size));
    }

    @GetMapping("/solving/{uuid}/status")
    public Integer getSolvingStatus(@PathVariable("uuid") String uuid){
        return solveService.getSolvingStatus(uuid);
    }

    @GetMapping("/solving/{uuid}/result")
    public ResponseEntity<InputStreamResource> getResultImage(@PathVariable("uuid") String uuid) throws IOException {
        return solveService.getResultImage(uuid);        
    }
}
