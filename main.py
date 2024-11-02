<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Cubo 3D al estilo Matrix</title>
    <style>
        body { margin: 0; background-color: black; }
        canvas { display: block; }
    </style>
</head>
<body>
    <!-- Incluimos la biblioteca Three.js desde un CDN -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // Crear la escena y la cámara
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x000000);

        const camera = new THREE.PerspectiveCamera(
            75, window.innerWidth / window.innerHeight, 0.1, 1000
        );

        // Crear el renderizador
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // Crear el cubo con líneas verdes
        const geometry = new THREE.BoxGeometry();
        const edges = new THREE.EdgesGeometry(geometry);
        const material = new THREE.LineBasicMaterial({ color: 0x00ff00 });
        const cube = new THREE.LineSegments(edges, material);
        scene.add(cube);

        camera.position.z = 5;

        // Función de animación
        function animate() {
            requestAnimationFrame(animate);

            // Rotar el cubo
            cube.rotation.x += 0.01;
            cube.rotation.y += 0.01;

            renderer.render(scene, camera);
        }
        animate();

        // Ajustar la ventana al cambiar el tamaño
        window.addEventListener('resize', function () {
            const width = window.innerWidth;
            const height = window.innerHeight;
            renderer.setSize(width, height);
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
        });
    </script>
</body>
</html>
