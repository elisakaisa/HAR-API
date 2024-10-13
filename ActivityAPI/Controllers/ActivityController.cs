using ActivityAPI.Models;
using Microsoft.AspNetCore.Mvc;
using Grpc.Net.Client;
using ActivityPredictor;

namespace ActivityAPI.Controllers;

[ApiController]
[Route("[controller]")]
public class ActivityController : ControllerBase 
{
    private readonly ILogger<ActivityController> _logger;

    public ActivityController(ILogger<ActivityController> logger)
    {
        _logger = logger;
    }

    [HttpGet(Name = "GetActivity")]
    public async Task<Prediction> Get()
    {
        var channel = GrpcChannel.ForAddress("http://localhost:50051");

        // Create a client for the ActivityPredictor service
        var client = new ActivityPredictor.ActivityPredictor.ActivityPredictorClient(channel);

        // Create the request object
        var request = new AddRequest
        {
            Num1 = 5,
            Num2 = 10
        };

        // Call the Add method on the server
        var response = await client.AddAsync(request);
        var prediction = new Prediction
        {
            Activity = response.Result.Activity,
            Accuracy = response.Result.Accuracy
        
        };
        return prediction;
    }
}