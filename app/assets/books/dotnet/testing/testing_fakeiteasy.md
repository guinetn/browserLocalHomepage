# FAKEITEASY

https://fakeiteasy.github.io/


using Xunit;
using FakeItEasy;

[Fact]
public void TestGetQuality_HS_KO()
{
    var service = new Supervision(GetContext());

    var quality = service.Quality(10, State.HS);
    Assert.Equal(Quality.KO, quality);

    var parameters = new List<IParameter>();
    IParameter parameter;

    parameter = A.Fake<IParameter>();
    A.CallTo(() => parameter.Name).Returns("R.A");
    A.CallTo(() => parameter.Value).Returns("0.9");
    parameters.Add(parameter);

    parameter = A.Fake<IParameter>();
    A.CallTo(() => parameter.Name).Returns("R.B");
    A.CallTo(() => parameter.Value).Returns("0.1");
    parameters.Add(parameter);
}




