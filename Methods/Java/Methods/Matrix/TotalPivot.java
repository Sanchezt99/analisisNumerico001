package Methods.Matrix;

import Errors.MatrixWithColumnZero;
import Errors.NoDimensionMatrix;
import Errors.NotSquareMatrix;
import Share.MatrixUtil;

public class TotalPivot extends PartialPivot{

    private int[] positionStamp;

    @Override
    public double[] execute(double[][] matrix, double[] b, boolean print) throws NotSquareMatrix, NoDimensionMatrix, MatrixWithColumnZero {

        initPositionStamp(matrix.length);
        return sort(super.execute(matrix, b, print), positionStamp);
    }

    void pivot(double[][] matrix, int index, double[] b) {
        int row = index;
        int col = index;

        for (int i = row; i < matrix.length; ++i) {
            for (int j = col; j < matrix.length; ++j) {
                if (Math.abs(matrix[j][i]) > Math.abs(matrix[row][col])) {
                    row = j;
                    col = i;
                }
            }
        }
        if (col != index) {
            MatrixUtil.swapColumns(matrix, col, index);
            MatrixUtil.swapValues(positionStamp, col, index);
        }
        if (row != index) {
            MatrixUtil.swapRows(matrix, row, index);
            MatrixUtil.swapValues(b, row, index);
        }
        System.out.println(row + "," + col);
    }

    private void initPositionStamp(int length) {
        if (positionStamp == null) {
            positionStamp = new int[length];
            for (int i = 0; i < length; i++) {
                positionStamp[i] = i;
            }
        }
    }

    private double[] sort(double[] values, int[] positions) {
        double[] sortedValues = new double[values.length];

        for (int i = 0; i < positions.length; ++i)
            sortedValues[positions[i]] = values[i];

        return sortedValues;
    }

    @Override
    public String toString() {
        return "Total Pivot: ";
    }
}
