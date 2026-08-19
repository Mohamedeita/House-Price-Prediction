import { Link, useLocation } from "react-router-dom";

function ResultPage() {
  const location = useLocation();

  const predictedPrice = location.state?.predicted_price;

  if (predictedPrice === undefined) {
    return (
      <main className="result-page">
        <div className="result-card">
          <h1>No Prediction Found</h1>

          <p>Please make a prediction first.</p>

          <Link to="/" className="back-button">
            Back to Prediction
          </Link>
        </div>
      </main>
    );
  }

  // INR → USD
  const exchangeRate = 95.7;

  const predictedPriceUSD = predictedPrice / exchangeRate;

  const formattedPrice = new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: 0,
  }).format(predictedPriceUSD);

  return (
    <main className="result-page">
      <div className="result-card">
        <h1>Predicted House Price</h1>

        <div className="price">
          {formattedPrice}
        </div>

        <p>
          Estimated property value based on the information
          you provided.
        </p>

        <Link to="/" className="back-button">
          Predict Another Property
        </Link>
      </div>
    </main>
  );
}

export default ResultPage;