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
public class Grid {
    public Grid(int length, int[][] rawGrid) {
        size = length;
        grid = new Integer[size][size];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                grid[i][j] = rawGrid[i][j];
            }
        }
    }
    Integer size;
    Integer[][] grid;
}
