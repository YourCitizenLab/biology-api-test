import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#18212f",
        panel: "#f8fafc",
        safety: "#b42318",
        signal: "#0f766e",
        amberline: "#b7791f",
      },
      boxShadow: {
        surface: "0 14px 36px rgba(15, 23, 42, 0.09)",
      },
    },
  },
  plugins: [],
};

export default config;
