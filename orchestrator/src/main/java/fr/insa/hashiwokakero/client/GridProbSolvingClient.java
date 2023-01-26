package fr.insa.hashiwokakero.client;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.List;

import fr.insa.hashiwokakero.modele.solving.GridProb;
import fr.insa.hashiwokakero.modele.solving.SolvedGridNode;

@FeignClient(name = "solving-prob", url = "${client.solving-prob.url}")
public interface GridProbSolvingClient {

    @PostMapping("/solve")
    public List<List<SolvedGridNode>> solve(@RequestBody GridProb grid);
}
