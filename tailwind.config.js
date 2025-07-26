 module.exports = {
       content: [
         './templates/**/*.html', // Path to your Flask templates
         // Add other paths if you have dynamic content or JS files using Tailwind classes
       ],
       theme: {
         extend: {},
       },
       plugins: [
         require('daisyui'),
       ],
       daisyui: {
         themes: ["light", "dark", "cupcake"], // Customize your themes
       }
     }