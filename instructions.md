# Guide To Getting Started

_N/B: Only meant for Administration access_

## Installing Python Dependancies
```bash
python -m pip install -r requirements.txt
```

## Material Tailwind with Flask
### Core
```bash
npm install -D tailwindcss
npx tailwindcss init
``` 
    OR
```bash
npm install tailwindcss@3 --save-dev
npx tailwindcss init
```
# Compile 
```bash
npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/out.css --watch
```
### Using NPM
```bash
npm i @material-tailwind/html
```

_Reference On Installation Guide_
https://www.material-tailwind.com/docs/html/guide/flask