import React, { useState, useEffect } from 'react';

const WaveVisualization = () => {
  const [time, setTime] = useState(0);
  const width = 600;
  const height = 300;

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(t => (t + 0.1) % 100);
    }, 50);
    return () => clearInterval(timer);
  }, []);

  const points = [];
  for(let x = 0; x < width; x += 5) {
    // Première onde
    const wave1 = Math.sin(x/30 - time) * 20;
    // Deuxième onde (fréquence différente)
    const wave2 = Math.sin(x/50 - time * 1.5) * 15;
    // Combinaison des ondes
    const combined = wave1 + wave2;
    points.push({x, y: height/2 + combined});
  }

  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <h3 className="text-lg font-bold mb-4">Superposition de deux ondes</h3>
      <svg width={width} height={height} className="border border-gray-200">
        {/* Axe horizontal */}
        <line x1="0" y1={height/2} x2={width} y2={height/2} stroke="#ddd" />
        
        {/* Première onde en bleu clair */}
        <path
          d={points.map((p, i) => `${i === 0 ? 'M' : 'L'} ${p.x},${height/2 + Math.sin(p.x/30 - time) * 20}`).join(' ')}
          stroke="lightblue"
          fill="none"
        />
        
        {/* Deuxième onde en rose clair */}
        <path
          d={points.map((p, i) => `${i === 0 ? 'M' : 'L'} ${p.x},${height/2 + Math.sin(p.x/50 - time * 1.5) * 15}`).join(' ')}
          stroke="pink"
          fill="none"
        />
        
        {/* Onde combinée en violet */}
        <path
          d={points.map((p, i) => `${i === 0 ? 'M' : 'L'} ${p.x},${p.y}`).join(' ')}
          stroke="purple"
          strokeWidth="2"
          fill="none"
        />
      </svg>
      <div className="mt-2 text-sm">
        <div className="flex items-center">
          <div className="w-4 h-4 bg-blue-200 mr-2"></div>
          <span>Première onde</span>
        </div>
        <div className="flex items-center">
          <div className="w-4 h-4 bg-pink-200 mr-2"></div>
          <span>Deuxième onde</span>
        </div>
        <div className="flex items-center">
          <div className="w-4 h-4 bg-purple-500 mr-2"></div>
          <span>Combinaison des deux ondes</span>
        </div>
      </div>
    </div>
  );
};

