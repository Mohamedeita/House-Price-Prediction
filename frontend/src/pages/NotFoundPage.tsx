import { Link } from "react-router-dom";

function NotFoundPage() {
  return (
    <main className="result-page">
      <div className="result-card">
        <h1>404</h1>

        <p>Page not found.</p>

        <Link to="/" className="back-button">
          Go Home
        </Link>
      </div>
    </main>
  );
}

export default NotFoundPage;