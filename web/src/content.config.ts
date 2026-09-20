import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "zod";

const recordedNumber = z.union([z.number(), z.literal("unknown")]);

const recipes = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "../recipes" }),
  schema: z.object({
    id: z.string(),
    title: z.string(),
    status: z.enum(["draft", "testing", "trusted"]),
    servings: recordedNumber,
    prep_time_minutes: recordedNumber,
    cook_time_minutes: recordedNumber,
    total_time_minutes: recordedNumber,
    tags: z.array(z.string()),
    source: z.string(),
    updated: z.union([z.string(), z.date()]),
    schema_version: z.number(),
  }),
});

export const collections = { recipes };
