package fr.insa.hashiwokakero.client;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;

import fr.insa.hashiwokakero.modele.solving.GridProb;


@FeignClient(name = "recognize", url = "${client.recognition.url}")
public interface ImageRecognitionClient {
    
    @PostMapping(path ="/recognize", consumes=MediaType.IMAGE_JPEG_VALUE)
    GridProb recognize(@RequestBody byte[] image, @RequestParam("size") int size);

}
