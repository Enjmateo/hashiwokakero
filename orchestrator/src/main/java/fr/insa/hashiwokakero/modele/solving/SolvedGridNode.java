package fr.insa.hashiwokakero.modele.solving;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@ToString
public class SolvedGridNode {
    Integer horizontal = 0;
    Integer vertical = 0;

    Integer bottom = 0;
    Integer top = 0;
    Integer left = 0;
    Integer right = 0;
    Integer k = 0;
}
