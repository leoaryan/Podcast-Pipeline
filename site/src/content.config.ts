import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const digests = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/digests' }),
  schema: z.object({
    title: z.string(),
    channel: z.string(),
    guest: z.string().optional().default(''),
    published: z.date(),
    analyzed: z.date(),
    duration_minutes: z.number(),
    topics: z.array(z.enum(['ai-research', 'engineering', 'policy-society', 'business', 'science-health', 'wildcard'])),
    source_url: z.string().optional().default(''),
  }),
});

export const collections = { digests };
