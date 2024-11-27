<h1>Project Setup</h1>
<p>Follow the instructions below to set up and run the project.</p>

<h2>1. Clone the repository</h2>
<p>First, clone the repository by running the following command:</p>
<pre><code>git clone <strong>[your-git-repository-url](https://github.com/mjavadvali/task_project.git)</strong></code></pre>

<h2>2. Build and start the Docker containers</h2>
<p>Navigate to the project directory and run the following command to build and start the containers:</p>
<pre><code>docker-compose up -d --build</code></pre>

<h2>3. Create a superuser</h2>
<p>Once the containers are running, you can create a superuser for Django admin by running:</p>
<pre><code>docker exec -it task_project-backend-1 python manage.py createsuperuser</code></pre>

<h2>4. Accessing API Endpoints</h2>
<p>To access API endpoints, you need to include the token that you receive by making a POST request to <code>/api/auth/token/</code> in your API requests.</p>
<p>Include the token in the <strong>Authorization</strong> header of your request:</p>
<pre><code>Authorization: Token &lt;your-token-here&gt;</code></pre>


<p>Example of a request in Rester:</p
![Capture](https://github.com/user-attachments/assets/67fde6d0-3630-4df7-83b1-70841eeb0324)
