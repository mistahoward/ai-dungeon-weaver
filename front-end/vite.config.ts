import { sentryVitePlugin } from "@sentry/vite-plugin";
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react(), sentryVitePlugin({
    org: "alex-howard",
    project: "ai-dungeon-weaver-front-end"
  })],

  build: {
    sourcemap: true
  }
})