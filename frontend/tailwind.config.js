/** @type {import('tailwindcss').Config} */
import forms from "@tailwindcss/forms"

export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Fira Sans", "sans-serif"],
        display: ["Shrikhand", "serif"],
      },
    },
  },
  plugins: [forms],
}
