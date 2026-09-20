# Chef OS web

This Astro site renders the canonical recipe files from `../recipes`. It never stores a second copy of recipe data.

## Local development

```bash
cd web
npm install
npm run dev
```

The production build is published to GitHub Pages by `.github/workflows/deploy-pages.yml` whenever recipe or web files change.

Ingredient scaling is enabled only after a recipe records a numeric `servings` value. Draft recipes remain visible but carry an explicit warning.
