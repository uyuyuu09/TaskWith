export default defineNuxtConfig({
	ssr: true,
	compatibilityDate: '2024-04-03',
	devtools: { enabled: true },
	css: ['/static/css/main.css'],
	postcss: {
		plugins: {
			tailwindcss: {},
			autoprefixer: {},
		},
	},
	app: {
		head: {
			htmlAttrs: {
				lang: 'ja',
				prefix: 'og: http://ogp.me/ns#',
			},
			charset: 'utf-8',
			viewport: 'width=device-width, initial-scale=1',
			title: 'TaskWith',
		},
	},
	modules: [
		'@pinia/nuxt',
		'@pinia-plugin-persistedstate/nuxt',
	],
});
