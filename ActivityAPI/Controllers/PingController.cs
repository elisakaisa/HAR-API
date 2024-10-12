using ActivityAPI.Models;
using Microsoft.AspNetCore.Mvc;

namespace ActivityAPI.Controllers;

[ApiController]
[Route("[controller]")]
public class PingController : ControllerBase 
{
    private readonly ILogger<PingController> _logger;

    public PingController(ILogger<PingController> logger)
    {
        _logger = logger;
    }

    [HttpGet(Name = "Ping")]
    public Ping Get()
    {
        return new Ping 
        {
            DateTime = DateTime.UtcNow,
            Working = true
        };
    }
}