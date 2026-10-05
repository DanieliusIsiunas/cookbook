import type { CollectionEntry } from "astro:content";

type Recipe = CollectionEntry<"recipes">;

export const statusLabels = {
  trusted: "Cooked and trusted",
  testing: "Testing",
  draft: "Draft",
} as const;

export const statusRank = { trusted: 0, testing: 1, draft: 2 } as const;

export function recipeExcerpt(recipe: Recipe) {
  const match = recipe.body?.match(/## Intended result\s+([\s\S]*?)(?=\n## |$)/);
  return (match?.[1] ?? "Open the recipe to review its current notes.")
    .replace(/\[(.*?)\]\(.*?\)/g, "$1")
    .replace(/[*_`#]/g, "")
    .replace(/\s+/g, " ")
    .trim();
}

export function recipeImage(recipe: Recipe, base: string) {
  if (recipe.data.id === "beef-pork-lasagna-ricotta") {
    return `${base}images/beef-pork-lasagna-ricotta.webp`;
  }
  if (recipe.data.id === "creamy-guanciale-tagliatelle") {
    return `${base}images/creamy-guanciale-tagliatelle.webp`;
  }
  return null;
}

export function timeLabel(recipe: Recipe) {
  const total = recipe.data.total_time_minutes;
  if (typeof total === "number") return `${total} min total`;

  const cook = recipe.data.cook_time_minutes;
  if (typeof cook === "number") return `${cook} min cooking`;

  return "Time to be recorded";
}

export function formattedDate(value: string | Date) {
  const date = value instanceof Date ? value : new Date(`${value}T00:00:00`);
  return new Intl.DateTimeFormat("en-GB", {
    day: "numeric",
    month: "short",
    year: "numeric",
  }).format(date);
}

export function sourcePath(recipe: Recipe) {
  const fromFile = recipe.filePath?.split("/recipes/")[1];
  return fromFile ?? `${recipe.data.tags[0]}/${recipe.data.id}.md`;
}

export function detectAllergens(recipe: Recipe) {
  const text = recipe.body?.toLowerCase() ?? "";
  const allergens: string[] = [];

  if (/\b(milk|butter|cheese|ricotta|mozzarella|cream|yoghurt|yogurt)\b/.test(text)) {
    allergens.push("milk");
  }
  if (/\b(egg|eggs)\b/.test(text)) allergens.push("eggs");
  if (/\b(flour|pasta|lasagne|lasagna|wheat|bread)\b/.test(text)) allergens.push("gluten");
  if (/\b(peanut|peanuts)\b/.test(text)) allergens.push("peanuts");
  if (/\b(almond|hazelnut|walnut|cashew|pistachio|pecan)\b/.test(text)) allergens.push("tree nuts");

  return allergens;
}
