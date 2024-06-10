<h1>URL Shortener Project Documentation</h1>

<h2>Introduction</h2>
<p>This project is a URL shortener application that allows users to shorten long URLs, track the number of clicks, and see the expiration date of the shortened URLs. It includes an API for backend operations and a frontend interface for user interaction.</p>

<h2>Modules Overview</h2>

<h3>API Module</h3>
<p>The API module handles the core functionality of the URL shortener application. It includes models, serializers, views, permissions, and URL routing.</p>

<ul>
    <li><strong>models.py:</strong> Defines the <code>Shorterlink</code> model, which stores information about the original URL, the shortened URL, click count, last click date, and expiration date. It includes utility functions to generate short links and expiration dates.</li>
    <li><strong>serializers.py:</strong> Contains the <code>ShortlinkSerializer</code>, which converts the <code>Shorterlink</code> model instances to JSON format and vice versa.</li>
    <li><strong>views.py:</strong> Implements the API views for creating, retrieving, updating, and deleting shortened URLs. The main views are:
        <ul>
            <li><code>ShorterlinkCreateAPIView:</code> Handles the creation of new shortened URLs.</li>
            <li><code>ShorterlinkListAPIView:</code> Lists all shortened URLs for the authenticated user.</li>
            <li><code>ShorterlinkDetailAPIView:</code> Retrieves details of a specific shortened URL.</li>
            <li><code>ShorterlinkUpdateView:</code> Updates a specific shortened URL.</li>
            <li><code>ShorterlinkDeleteView:</code> Deletes a specific shortened URL.</li>
        </ul>
    </li>
    <li><strong>permissions.py:</strong> Defines custom permissions:
        <ul>
            <li><code>IsAdminOrOwner:</code> Allows access to admin users or the owner of the URL.</li>
            <li><code>AllowAnyCreate:</code> Allows any user to create a shortened URL.</li>
        </ul>
    </li>
    <li><strong>urls.py:</strong> Configures the URL routing for the API endpoints.</li>
</ul>

<h3>Frontend Module</h3>
<p>The frontend module provides the user interface for interacting with the URL shortener application. It includes views, templates, static files, and URL routing.</p>

<ul>
    <li><strong>views.py:</strong> Contains the view function <code>index</code> that renders the main page of the frontend.</li>
    <li><strong>templates/frontend:</strong> Includes the HTML templates for the frontend. The main templates are:
        <ul>
            <li><code>index.html:</code> The main page template where users can input URLs to be shortened.</li>
            <li><code>base.html:</code> The base template that includes common elements like the header and footer.</li>
            <li><code>navbar.html:</code> The navigation bar template.</li>
        </ul>
    </li>
    <li><strong>static/frontend/js/api_requests.js:</strong> Contains JavaScript code to handle form submissions, send requests to the API, and update the frontend with the response data.</li>
</ul>

<h3>Main Application Configuration</h3>
<p>This section includes the main configuration for the Django project.</p>

<ul>
    <li><strong>linkshortener/urls.py:</strong> Configures the URL routing for the entire project, including the API and frontend modules. It also sets up the Swagger documentation views.</li>
    <li><strong>settings.py:</strong> Contains the Django settings for the project, such as installed apps, middleware, and database configuration.</li>
</ul>

<h3>Redirection Module</h3>
<p>The redirection module handles the functionality of redirecting users from the shortened URL to the original URL.</p>

<ul>
    <li><strong>views.py:</strong> Contains the view function <code>url_redirection</code> that processes the redirection. It increments the click count, updates the last click date, and checks the expiration date before performing the redirection.</li>
    <li><strong>urls.py:</strong> Configures the URL routing for the redirection functionality.</li>
</ul>

<h2>How It Works</h2>
<p>Users can enter a long URL in the frontend interface. The frontend sends a POST request to the API with the original URL. The API checks if the URL has already been shortened; if not, it creates a new shortened URL, saves it to the database, and returns the shortened URL along with other details like click count and expiration date. The frontend displays this information to the user. When a user visits the shortened URL, the redirection module handles the request, updates the click count and last click date, checks if the URL has expired, and then redirects the user to the original URL.</p>


