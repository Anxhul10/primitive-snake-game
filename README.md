<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>primitive-snake-game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f0f0f0;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            font-size: 28px;
            color: #333;
            margin-bottom: 20px;
            text-align: center;
        }

        .demo-img {
            display: block;
            margin: 0 auto;
            max-width: 100%;
            height: auto;
            border-radius: 5px;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
        }

        .code-block {
            background-color: #f5f5f5;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 20px;
            white-space: pre-wrap;
            overflow-x: auto;
        }

        pre {
            margin: 0;
        }

        ul {
            list-style-type: disc;
            padding-left: 20px;
        }

        li {
            margin-bottom: 5px;
        }

        p {
            margin-bottom: 15px;
        }

        .text-center {
            text-align: center;
        }

        .text-bold {
            font-weight: bold;
        }

        .highlight {
            color: #007bff;
        }

        .link {
            color: #007bff;
            text-decoration: none;
        }

        .link:hover {
            text-decoration: underline;
        }

        .license {
            margin-top: 20px;
            font-size: 14px;
            color: #666;
        }

        .license a {
            color: #666;
            text-decoration: none;
        }

        .license a:hover {
            text-decoration: underline;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>primitive-snake-game</h1>

        <img src="demo.gif" alt="Snake Game Demo" class="demo-img">

        <p>An old-school snake game created using Python, perfect for beginners looking to delve into game development
            with Python.</p>

        <h2>Features</h2>
        <ul>
            <li>Classic snake gameplay where the player controls a snake to eat food and grow in size.</li>
            <li>Simple yet engaging gameplay mechanics.</li>
            <li>Written in Python, making it easy to understand and modify for learning purposes.</li>
        </ul>

        <h2>How to Run</h2>
        <ol>
            <li><strong>Clone the Repository:</strong>
                <div class="code-block">
                    <pre>git clone https://github.com/your-username/primitive-snake-game.git</pre>
                </div>
                Replace <span class="text-bold">your-username</span> with your GitHub username.
            </li>
            <li><strong>Navigate to the Directory:</strong>
                <div class="code-block">
                    <pre>cd primitive-snake-game</pre>
                </div>
            </li>
            <li><strong>Open in IDE:</strong>
                <ul>
                    <li>Open <code>main.py</code> in your preferred Python IDE (e.g., PyCharm, VS Code, Spyder).</li>
                </ul>
            </li>
            <li><strong>Run the Game:</strong>
                <ul>
                    <li>Execute the <code>main.py</code> file and enjoy playing!</li>
                </ul>
            </li>
        </ol>

        <h2>Controls</h2>
        <p>Use the arrow keys (<span class="text-bold">↑</span>, <span class="text-bold">↓</span>,
            <span class="text-bold">←</span>, <span class="text-bold">→</span>) to control the snake's direction.</p>

        <h2>Requirements</h2>
        <ul>
            <li>Python 3.x</li>
            <li>No additional Python packages required.</li>
        </ul>

        <h2>Contributing</h2>
        <p>Contributions are welcome! Fork the repository, make your improvements, and create a pull request. Issues and
            feature requests can be submitted via <a href="https://github.com/your-username/primitive-snake-game/issues"
                class="link">GitHub issues</a>.</p>

        <h2>License</h2>
        <p class="license">This project is licensed under the <a href="LICENSE" class="link">MIT License</a> - see the
            <a href="LICENSE" class="link">LICENSE</a> file for details.</p>

        <h2>Acknowledgments</h2>
        <ul>
            <li>Built following tutorials and guides for basic game development in Python.</li>
            <li>Inspired by the nostalgia of classic snake games.</li>
        </ul>

        <p class="text-center">Feel free to customize it further to match the specific details of your project and personal
            style!</p>
    </div>
</body>

</html>
