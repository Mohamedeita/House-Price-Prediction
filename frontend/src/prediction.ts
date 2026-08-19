export interface PredictionRequest {
  location: string;
  Status: string;
  Transaction: string;
  Furnishing: string;
  facing: string;
  Ownership: string;
  Bathroom: number;
  Balcony: number;
  Carpet_Area_sqft: number;
  Super_Area_sqft: number;
  Car_Parking_Count: number;
  Current_Floor: number;
  Total_Floors: number;
  Has_Main_Road: number;
  Has_Garden_Park: number;
  Has_Pool: number;
  Society_Frequency: number;
}

export interface PredictionResponse {
  predicted_price: number;
}