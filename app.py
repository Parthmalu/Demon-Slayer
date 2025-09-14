from flask import Flask, render_template_string, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

home_page = '''
<!doctype html>
<html lang="en">
<head>
  <title>Movie with me?</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');
    body {
      margin: 0;
      padding: 0;
      height: 100vh;
      background: url('https://media.giphy.com/media/Nx0rz3jtxtEre/giphy.gif') no-repeat center center fixed;
      background-size: cover;
      font-family: 'Poppins', sans-serif;
      color: white;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-shadow: 2px 2px 6px black;
      overflow-x: hidden;
      user-select: none;
    }
    h1 {
      font-size: 4rem;
      margin-bottom: 20px;
      background: rgba(0,0,0,0.6);
      padding: 12px 24px;
      border-radius: 15px;
      transition: transform 0.3s ease;
    }
    .button-container {
      margin: 20px;
      display: flex;
      gap: 30px;
      user-select: none;
    }
    button {
      font-size: 1.6rem;
      padding: 14px 40px;
      border: none;
      border-radius: 15px;
      cursor: pointer;
      transition: transform 0.2s ease, box-shadow 0.3s ease;
      color: white;
      box-shadow: 2px 6px 10px rgba(0,0,0,0.7);
      background-color: #28a745;
      font-weight: 600;
      outline-offset: 4px;
      outline-color: transparent;
    }
    button:hover {
      background-color: #218838;
      transform: scale(1.1);
      box-shadow: 0 0 18px #28a745;
      outline-color: #28a745;
    }
    button:active {
      transform: scale(0.95);
      box-shadow: 0 0 8px #1e7e34;
    }
    button.no {
      background-color: #dc3545;
    }
    button.no:hover {
      background-color: #c82333;
      box-shadow: 0 0 18px #dc3545;
    }
    .error-message {
      margin-top: 10px;
      font-weight: 700;
      font-size: 1.4rem;
      color: #ff4444;
      background: rgba(0,0,0,0.7);
      border-radius: 10px;
      padding: 8px 20px;
      opacity: 0;
      animation: fadeIn 0.8s forwards;
      user-select: none;
      pointer-events: none;
      position: absolute;
      top: 20px;
      left: 50%;
      transform: translateX(-50%);
      white-space: nowrap;
      box-shadow: 0 0 6px #ff4444;
      font-family: monospace;
    }
    .error-message.active {
      opacity: 1;
      pointer-events: auto;
      animation: shake 0.6s;
    }
    img.demon-slayer-gif {
      max-width: 320px;
      margin-top: 40px;
      border-radius: 15px;
      box-shadow: 0 0 25px #ff4500;
      user-select: none;
      transition: transform 0.4s ease;
    }
    img.demon-slayer-gif:hover {
      transform: scale(1.05) rotate(3deg);
      box-shadow: 0 0 30px #ff6a00;
    }
    /* Shaking animation for No button */
    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      20%, 60% { transform: translateX(-8px); }
      40%, 80% { transform: translateX(8px); }
    }
    /* Fade in */
    @keyframes fadeIn {
      to { opacity: 1; }
    }
    /* Loading spinner */
    .spinner {
      margin-top: 30px;
      border: 6px solid rgba(255, 69, 0, 0.2);
      border-top: 6px solid #ff4500;
      border-radius: 50%;
      width: 60px;
      height: 60px;
      animation: spin 1s linear infinite;
      display: none;
      user-select: none;
    }
    @keyframes spin {
      100% { transform: rotate(360deg); }
    }
    /* Countdown text */
    .countdown-text {
      margin-top: 20px;
      font-size: 1.5rem;
      font-weight: 700;
      background: rgba(0,0,0,0.6);
      border-radius: 12px;
      padding: 6px 20px;
      box-shadow: 0 0 10px #ff6a00;
      user-select: none;
      display: none;
      user-select:none;
    }
    /* Responsive */
    @media (max-width: 480px) {
      h1 {
        font-size: 2.8rem;
        padding: 8px 16px;
      }
      button {
        font-size: 1.2rem;
        padding: 10px 25px;
      }
      img.demon-slayer-gif {
        max-width: 90vw;
      }
    }
  </style>
</head>
<body>
  <h1>Movie with me?</h1>
  
  <form id="choiceForm" method="post" action="/">
    <div class="button-container">
      <button type="button" class="yes" id="yesBtn">Yes</button>
      <button type="button" class="no" id="noBtn">No</button>
    </div>
  </form>

  <p id="errorMsg" class="error-message">TRY PRESSING YES</p>
  <div class="spinner" id="spinner"></div>
  <p class="countdown-text" id="countdown">Redirecting in 5 seconds...</p>

  <img class="demon-slayer-gif" src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDJrN2o0MWhiemd3dHpqdXpiODlhbzI4c3MxZmV1YmZrMHFxZ2V4YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/R9TbpugxAhx9UnerhD/giphy.gif" alt="Demon Slayer GIF">

<script>
  const yesBtn = document.getElementById('yesBtn');
  const noBtn = document.getElementById('noBtn');
  const errorMsg = document.getElementById('errorMsg');
  const spinner = document.getElementById('spinner');
  const countdown = document.get

