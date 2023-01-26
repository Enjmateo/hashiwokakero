package fr.insa.hashiwokakero.client;

import java.util.List;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;

import fr.insa.hashiwokakero.modele.solving.SolvedGridNode;

@FeignClient(name = "image-creation", url = "${client.image-creation.url}")
public interface ImageCreationClient {
    
    @PostMapping("/create-image")
    public @ResponseBody byte[] createImage(@RequestBody List<List<SolvedGridNode>> solvedGrid);
}
