const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: "/", // Ajustez si nécessaire pour le chemin public
  configureWebpack: {
    entry: "./src/main.js",
    devtool: "source-map", // Active les source maps
  },
  devServer: {
    hot: true,
    // port: 8080, // Utilise le port que tu exposes dans Docker
    port: 3000, // Utilise le port que tu exposes dans Docker
    host: "0.0.0.0", // Bind à toutes les interfaces réseau pour Docker
    client: {
      webSocketURL: "ws://localhost:3000/ws", // WebSocket via le port 3000 sur l'hôte
    },
    // watch: true,
    // watchOptions: {
    //   ignored: /node_modules/,
    //   poll: 1000,
    // },

    watchFiles: {
      paths: ["src/**/*", "public/**/*"], // Surveille les changements dans ces dossiers
      options: {
        usePolling: true, // Utilise le mode polling pour détecter les changements
      },
    },
  },
});
