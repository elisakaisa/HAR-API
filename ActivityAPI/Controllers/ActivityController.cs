using ActivityAPI.Models;
using Microsoft.AspNetCore.Mvc;
using ActivityPredictor;
using Grpc.Core;

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
        //TODO: turn thids into post request
        var testActivitydata = new ActivityData();

        var headers = new Metadata
        {
            { "api-key", "wrongapikey" }  // Add your API key here
        };

        // Create the request object
        var request = new AddRequest
        {
            Data = testActivitydata.Serialize(),
            Rows = 300,
            Columns = 6
        };

        try 
        {
            var response = await _client.AddAsync(request, headers: headers);
            var prediction = new Prediction
            {
                Activity = response.Result.Activity,
                Accuracy = response.Result.Accuracy
            
            };
            return Ok(prediction);

        }
        catch (RpcException e)
        {
            if (e.StatusCode == Grpc.Core.StatusCode.Unauthenticated) 
            {
                return Unauthorized(e.Status.Detail);
            }
            return StatusCode(500);
        }
        catch (Exception) 
        {
            return StatusCode(500);
        }
    }
}