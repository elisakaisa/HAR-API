using ActivityAPI.Models;
using Microsoft.AspNetCore.Mvc;
using ActivityPredictor;

namespace ActivityAPI.Controllers;

[ApiController]
[Route("[controller]")]
public class ActivityController : ControllerBase 
{
    private readonly ILogger<ActivityController> _logger;
    private readonly ActivityPredictor.ActivityPredictor.ActivityPredictorClient _client;

    public ActivityController(ILogger<ActivityController> logger, ActivityPredictor.ActivityPredictor.ActivityPredictorClient client)
    {
        _logger = logger;
        _client = client;
    }

    [HttpGet(Name = "GetActivity")]
    public async Task<IActionResult> Get()
    {
        // Create the request object
        var request = new AddRequest
        {
            Num1 = 5,
            Num2 = 10
        };

        // Call the Add method on the server
        var response = await _client.AddAsync(request);
        var prediction = new Prediction
        {
            Activity = response.Result.Activity,
            Accuracy = response.Result.Accuracy
        
        };
        return Ok(prediction);
    }
}