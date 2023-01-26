package fr.insa.hashiwokakero.modele.solving;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
@ToString
public class GridProb {
    public GridProb(int length, int[][][] rawGrid) {
        size = length;
        grid = new Integer[size][size][8];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                for (int k = 0; k < 8; k++) {
                    grid[i][j][k] = rawGrid[i][j][k];
                }
            }
        }
    }
    Integer size;
    Integer[][][] grid;
}
