import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { predictPrice } from "../api/predictionClient";
import type { PredictionRequest } from "../types/prediction";

function PredictionForm() {
  const navigate = useNavigate();

  const [locations, setLocations] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const [formData, setFormData] = useState<PredictionRequest>({
    location: "",
    Status: "Ready to Move",
    Transaction: "Resale",
    Furnishing: "Semi-Furnished",
    facing: "East",
    Ownership: "Freehold",
    Bathroom: 2,
    Balcony: 1,
    Carpet_Area_sqft: 1100,
    Super_Area_sqft: 1300,
    Car_Parking_Count: 1,
    Current_Floor: 2,
    Total_Floors: 5,
    Has_Main_Road: 1,
    Has_Garden_Park: 0,
    Has_Pool: 0,
    Society_Frequency: 100,
  });

  useEffect(() => {
    fetch("/locations.json")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to load locations");
        }
        return response.json();
      })
      .then((data) => {
        setLocations(data);
      })
      .catch(() => {
        setError("Could not load locations.");
      });
  }, []);

  const handleChange = (
    event: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) => {
    const { name, value } = event.target;

    const numericFields = [
      "Bathroom",
      "Balcony",
      "Carpet_Area_sqft",
      "Super_Area_sqft",
      "Car_Parking_Count",
      "Current_Floor",
      "Total_Floors",
      "Has_Main_Road",
      "Has_Garden_Park",
      "Has_Pool",
      "Society_Frequency",
    ];

    setFormData((previous) => ({
      ...previous,
      [name]: numericFields.includes(name) ? Number(value) : value,
    }));
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setError("");

    if (!formData.location) {
      setError("Please select a location.");
      return;
    }

    if (formData.Carpet_Area_sqft <= 0) {
      setError("Carpet area must be greater than 0.");
      return;
    }

    if (formData.Super_Area_sqft <= 0) {
      setError("Super area must be greater than 0.");
      return;
    }

    if (formData.Bathroom < 0 || formData.Balcony < 0) {
      setError("Bathrooms and balconies cannot be negative.");
      return;
    }

    try {
      setLoading(true);

      const result = await predictPrice(formData);

      navigate("/result", {
        state: {
          predicted_price: result.predicted_price,
        },
      });
    } catch {
      setError(
        "Prediction failed. Please make sure the backend is running on port 8000."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <form className="prediction-form" onSubmit={handleSubmit}>
      <h2>House Price Prediction</h2>

      {error && <div className="error-message">{error}</div>}

      <div className="form-grid">
        <div className="form-group">
          <label>Location</label>
          <select
            name="location"
            value={formData.location}
            onChange={handleChange}
            required
          >
            <option value="">Select location</option>

            {locations.map((location) => (
              <option key={location} value={location}>
                {location}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label>Status</label>
          <select
            name="Status"
            value={formData.Status}
            onChange={handleChange}
          >
            <option value="Ready to Move">Ready to Move</option>
            <option value="Under Construction">Under Construction</option>
          </select>
        </div>

        <div className="form-group">
          <label>Transaction</label>
          <select
            name="Transaction"
            value={formData.Transaction}
            onChange={handleChange}
          >
            <option value="Resale">Resale</option>
            <option value="New Property">New Property</option>
          </select>
        </div>

        <div className="form-group">
          <label>Furnishing</label>
          <select
            name="Furnishing"
            value={formData.Furnishing}
            onChange={handleChange}
          >
            <option value="Semi-Furnished">Semi-Furnished</option>
            <option value="Unfurnished">Unfurnished</option>
            <option value="Furnished">Furnished</option>
          </select>
        </div>

        <div className="form-group">
          <label>Facing</label>
          <select
            name="facing"
            value={formData.facing}
            onChange={handleChange}
          >
            <option value="East">East</option>
            <option value="West">West</option>
            <option value="North">North</option>
            <option value="South">South</option>
            <option value="North-East">North-East</option>
            <option value="North-West">North-West</option>
            <option value="South-East">South-East</option>
            <option value="South-West">South-West</option>
          </select>
        </div>

        <div className="form-group">
          <label>Ownership</label>
          <select
            name="Ownership"
            value={formData.Ownership}
            onChange={handleChange}
          >
            <option value="Freehold">Freehold</option>
            <option value="Leasehold">Leasehold</option>
          </select>
        </div>

        <div className="form-group">
          <label>Carpet Area (sqft)</label>
          <input
            type="number"
            name="Carpet_Area_sqft"
            value={formData.Carpet_Area_sqft}
            onChange={handleChange}
            min="1"
            required
          />
        </div>

        <div className="form-group">
          <label>Super Area (sqft)</label>
          <input
            type="number"
            name="Super_Area_sqft"
            value={formData.Super_Area_sqft}
            onChange={handleChange}
            min="1"
            required
          />
        </div>

        <div className="form-group">
          <label>Bathrooms</label>
          <input
            type="number"
            name="Bathroom"
            value={formData.Bathroom}
            onChange={handleChange}
            min="0"
            required
          />
        </div>

        <div className="form-group">
          <label>Balconies</label>
          <input
            type="number"
            name="Balcony"
            value={formData.Balcony}
            onChange={handleChange}
            min="0"
            required
          />
        </div>

        <div className="form-group">
          <label>Current Floor</label>
          <input
            type="number"
            name="Current_Floor"
            value={formData.Current_Floor}
            onChange={handleChange}
            min="0"
            required
          />
        </div>

        <div className="form-group">
          <label>Total Floors</label>
          <input
            type="number"
            name="Total_Floors"
            value={formData.Total_Floors}
            onChange={handleChange}
            min="1"
            required
          />
        </div>

        <div className="form-group">
          <label>Car Parking</label>
          <input
            type="number"
            name="Car_Parking_Count"
            value={formData.Car_Parking_Count}
            onChange={handleChange}
            min="0"
          />
        </div>

        <div className="form-group">
          <label>Society Frequency</label>
          <input
            type="number"
            name="Society_Frequency"
            value={formData.Society_Frequency}
            onChange={handleChange}
            min="0"
          />
        </div>

        <div className="form-group">
          <label>Main Road</label>
          <select
            name="Has_Main_Road"
            value={formData.Has_Main_Road}
            onChange={handleChange}
          >
            <option value="1">Yes</option>
            <option value="0">No</option>
          </select>
        </div>

        <div className="form-group">
          <label>Garden / Park</label>
          <select
            name="Has_Garden_Park"
            value={formData.Has_Garden_Park}
            onChange={handleChange}
          >
            <option value="1">Yes</option>
            <option value="0">No</option>
          </select>
        </div>

        <div className="form-group">
          <label>Swimming Pool</label>
          <select
            name="Has_Pool"
            value={formData.Has_Pool}
            onChange={handleChange}
          >
            <option value="1">Yes</option>
            <option value="0">No</option>
          </select>
        </div>
      </div>

      <button className="predict-button" type="submit" disabled={loading}>
        {loading ? "Predicting..." : "Predict Price"}
      </button>
    </form>
  );
}

export default PredictionForm;