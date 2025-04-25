# FinSight - Financial Analytics & GenAI Platform

## Project Overview
FinSight is a comprehensive financial analytics dashboard built with React that provides tools for financial forecasting, planning, market insights, and reporting. Developed by Team Rocket, this application leverages GenAI to transform financial data analysis and decision-making processes with a clean, responsive interface that works across desktop and mobile devices.

## Key Differentiators

- **No-Code Data Uploads**: Drag-and-drop CSV files or connect directly to Google Sheets
- **Interactive Dashboards**: Filter visualizations by region, department, or time horizon
- **User-Friendly Interface**: Built with React + Tailwind CSS for fast, responsive performance
- **AI-Powered Chatbot**: Natural language queries like "What's our forecasted cash flow next quarter?" deliver instant answers
- **Multi-Tenant Support**: Designed for SaaS delivery across multiple clients

## Features

- **Dashboard**: Main landing page with summary data and key performance indicators
- **Forecasting**: AI-powered tools for predicting future financial trends
- **Planning**: Interface for budget and financial planning with scenario analysis
- **Market Insights**: External market data analysis with AI-generated recommendations
- **Reports**: Financial reporting tools and templates with export capabilities

## Deployment Architecture Options

### Local Deployment
- **Environment**: Developer laptops or on-premises machines
- **Infrastructure**:
  - Local file storage (SQLite/CSV)
  - Local MLflow server
  - Local dashboard for visualization
- **Use Case**: Quick iteration, testing, offline inference

### Hybrid Deployment
- **Hosting**: Combination of local compute and cloud services (AWS)
- **Infrastructure**:
  - AWS RDS/Aurora or MongoDB for financial data
  - S3 for historical and batch data storage
  - Local ML model with fallback to AWS-hosted model
  - Frontend hosted on AWS Amplify
- **Use Case**: Balancing performance, cost-efficiency, partial cloud usage

### Full AWS Deployment (Pay-as-You-Go Cloud)
- **Hosting**: Fully hosted on AWS (serverless, scalable)
- **Infrastructure Components**:
  - Frontend: Next.js app on AWS Amplify
  - Backend: AWS Lambda, API Gateway
  - Model Management: MLflow Tracking Server on ECS Fargate
  - Model Hosting: SageMaker
- **Storage**:
  - RDS/Aurora (Transactional)
  - S3 (Batch, logs, historical data)
  - DynamoDB (KPI storage)
- **Monitoring**: CloudWatch

## Technology Stack

- **Frontend Framework**: React
- **Routing**: React Router
- **Styling**: Tailwind CSS
- **UI Components**: Headless UI
- **Icons**: Hero Icons
- **AI Integration**: GenAI capabilities for forecasting and insights
- **Database**: Support for various options including SQLite, MongoDB, AWS RDS/Aurora

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/finsight.git
   cd finsight
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm run dev
   ```

## Data Files

The application uses several CSV files for data:

- `customer_data.csv`: Customer demographic and behavior data
- `customer_purchases.csv`: Transaction history and purchase records
- `economic_indicators.csv`: External economic factors affecting financial forecasts
- `products.csv`: Product catalog with pricing and performance metrics
- `data_gen.ipynb`: Jupyter notebook for generating sample data

## Component Structure

### Main Components

- **Navigation.jsx**: Landing page with hero section and navigation
- **Navbar.jsx**: Responsive navigation bar used across all pages
- **Forecasting.jsx**: Financial forecasting interface with AI predictions
- **Planning.jsx**: Budget and strategic planning tools
- **MarketInsights.jsx**: Market analysis and competitive intelligence
- **Reports.jsx**: Financial reporting and document generation

## UI Design

The interface uses Tailwind CSS for styling with a clean, modern aesthetic:

- **Color Scheme**: Primary colors are indigo and white with accent gradients
- **Typography**: Modern sans-serif fonts with responsive sizing
- **Layout**: Responsive design with mobile-first approach
- **Components**: Custom buttons, cards, and navigation elements
- **Accessibility**: Designed for all users with proper contrast and semantic HTML

## Security Requirements

The application implements robust security measures to protect financial data:

- Data encryption at rest and in transit
- Role-based access controls
- Secure API endpoints with proper authentication
- Regular security audits and compliance checks
- Secure handling of sensitive financial information

## Future Development

Planned features for future releases:

1. Enhanced AI capabilities for more accurate financial forecasting
2. Integration with additional financial data sources and APIs
3. Advanced data visualization components with interactive modeling
4. Custom dashboards and widget creation
5. Mobile application for on-the-go financial insights
6. Expanded multi-tenant functionality for enterprise deployments

## Related Projects

There is a related retail analytics project in the codebase that includes:

- FastAPI backend with chat functionality
- RAG (Retrieval Augmented Generation) implementation
- Vector database for semantic search
- Template-based frontend

This retail component could potentially be integrated with FinSight for comprehensive retail financial analytics.

## Team Rocket

This project is developed by Team Rocket, focusing on Business Excellence through innovative financial technology solutions powered by GenAI.
