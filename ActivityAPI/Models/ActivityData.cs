using Google.Protobuf;

namespace ActivityAPI.Models;

public class ActivityData 
{
    public float[,] DataArray { get; set; }

    public ActivityData() 
    {
        DataArray = GenerateRandomData(300, 6);
    }

    
    public ByteString Serialize()
    {
        byte[] dataBytes = new byte[DataArray.Length * sizeof(float)];
        Buffer.BlockCopy(DataArray, 0, dataBytes, 0, dataBytes.Length);
        return ByteString.CopyFrom(dataBytes);;
    }

    private float[,] GenerateRandomData(int rows, int columns)
    {
        Random rand = new();

        // rand.NextDouble() generates a float in the range [0, 1).
        // Multiplying by 2 scales it to [0, 2).
        // Subtracting 1 shifts the range to [-1, 1)
        float[] flatData = Enumerable.Range(0, rows * columns)
            .Select(_ => (float)(rand.NextDouble() * 2 - 1))
            .ToArray();

        // Convert the flat array to a 2D array
        return To2DArray(flatData, rows, columns);
    }

    private static float[,] To2DArray(float[] array, int rows, int columns)
    {
        float[,] result = new float[rows, columns];
        for (int i = 0; i < array.Length; i++)
        {
            result[i / columns, i % columns] = array[i];
        }
        return result;
    }

}