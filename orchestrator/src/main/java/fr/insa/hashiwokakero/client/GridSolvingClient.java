package fr.insa.hashiwokakero.client;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.List;

import fr.insa.hashiwokakero.modele.solving.Grid;
import fr.insa.hashiwokakero.modele.solving.SolvedGridNode;

@FeignClient(name = "solving", url = "${client.solving.url}")
public interface GridSolvingClient {

    @PostMapping("/solve")
    public List<List<SolvedGridNode>> solve(@RequestBody Grid grid);
}
