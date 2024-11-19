document.addEventListener("DOMContentLoaded", () => {
  const canvas = document.getElementById("oceanCanvas");
  const ctx = canvas.getContext("2d");

  // 캔버스 크기 설정
  function resizeCanvas() {
      const container = document.getElementById("animationContainer");
      canvas.width = container.offsetWidth;
      canvas.height = container.offsetHeight;
  }

  resizeCanvas();

  const waveLines = [];
  const waveLineCount = 7;
  let waveOffset = 0;

  const fins = [];
  const finCount = 3;
  let finWaveOffset = 0;

  const dog = {
      x: canvas.width / 4,
      y: canvas.height / 2 - 100,
      width: 150,
      height: 150,
      speed: 2,
  };

  const dogImage = new Image();
  dogImage.src = "/static/dog_surfing.png";

  function initWaves() {
      waveLines.length = 0;
      for (let i = 0; i < waveLineCount; i++) {
          waveLines.push({
              y: canvas.height / 3 + i * 20,
              amplitude: 20 + Math.random() * 30,
              wavelength: 120 + Math.random() * 150,
              speed: 0.03 + Math.random() * 0.05,
              color: `rgba(255, 255, 255, ${0.4 + Math.random() * 0.2})`,
          });
      }
  }

  function initFins() {
      fins.length = 0;
      for (let i = 0; i < finCount; i++) {
          fins.push({
              x: Math.random() * canvas.width,
              y: canvas.height / 2 + Math.random() * 200 - 100,
              speed: 1.5 + Math.random() * 1.5,
              waveAmplitude: 15 + Math.random() * 15,
              size: 40 + Math.random() * 20,
          });
      }
  }

  function drawWaves() {
      waveOffset += 1;
      waveLines.forEach((wave, index) => {
          ctx.strokeStyle = wave.color;
          ctx.lineWidth = 2;
          ctx.beginPath();
          for (let x = 0; x < canvas.width; x++) {
              const y = wave.y + wave.amplitude * Math.sin((x + waveOffset) / wave.wavelength);
              if (x === 0) ctx.moveTo(x, y);
              else ctx.lineTo(x, y);
          }
          ctx.stroke();
      });
  }

  function drawFins() {
      finWaveOffset += 0.05;
      fins.forEach((fin) => {
          const finY = fin.y + Math.sin(finWaveOffset) * fin.waveAmplitude;
          const finWidth = fin.size;
          const finHeight = fin.size * 0.6;

          ctx.fillStyle = "#4682b4";
          ctx.beginPath();
          ctx.moveTo(fin.x, finY);
          ctx.quadraticCurveTo(fin.x + finWidth / 2, finY - finHeight, fin.x + finWidth, finY);
          ctx.quadraticCurveTo(fin.x + finWidth / 2, finY + finHeight / 2, fin.x, finY);
          ctx.fill();
      });
  }

  function drawDog() {
      ctx.drawImage(dogImage, dog.x - dog.width / 2, dog.y - dog.height / 2, dog.width, dog.height);
  }

  function updateDog() {
      dog.x += dog.speed;
      dog.y = canvas.height / 3 + waveLines[0].amplitude * Math.sin((dog.x + waveOffset) / waveLines[0].wavelength) - 20;

      if (dog.x > canvas.width) {
          dog.x = -dog.width;
      }
  }

  function animate() {
      ctx.fillStyle = "#87ceeb";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      drawWaves();
      drawFins();
      updateDog();
      drawDog();
      requestAnimationFrame(animate);
  }

  window.addEventListener("resize", () => {
      resizeCanvas();
      initWaves();
      initFins();
  });

  initWaves();
  initFins();
  animate();
});
