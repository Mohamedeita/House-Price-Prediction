import PredictionForm from "../components/PredictionForm";

function HomePage() {
  return (
    <main className="home-page">
      <header className="navbar">
        <div className="logo">
          House<span>Predict</span>
        </div>

        <div className="nav-label">
          AI House Price Prediction
        </div>
      </header>

      <section className="hero-section">
        <div className="hero-content">
          <p className="hero-tag">MACHINE LEARNING PROJECT</p>

          <h1>
            Predict Your
            <br />
            <span>House Price</span>
          </h1>

          <p className="hero-description">
            Enter your property details and our machine learning model
            will estimate its market price.
          </p>
        </div>
      </section>

      <section className="form-section">
        <div className="form-wrapper">
          <div className="section-heading">
            <p>PROPERTY DETAILS</p>
            <h2>Tell us about your property</h2>
          </div>

          <PredictionForm />
        </div>
      </section>

      <footer className="footer">
        <p>
          HousePredict — Machine Learning House Price Prediction
          

        </p>
         <p>
          
               Created by Mohamed Eita

        </p>

        <a
          href="https://www.linkedin.com/in/mohamed-eita-581187371"
          target="_blank"
          rel="noreferrer"
        >
          LinkedIn
        </a>
      </footer>
    </main>
  );
}

export default HomePage;