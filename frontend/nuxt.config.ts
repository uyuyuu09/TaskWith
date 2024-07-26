export default defineNuxtConfig({
	ssr: false,
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
		'@vite-pwa/nuxt',
	],
	image: {
		format: ['webp', 'png', 'svg'],
		dir: 'public/',
	},
	pinia: {
		storesDirs: ['./composables/**'],
	},
	piniaPersistedstate: {
		cookieOptions: {
			sameSite: 'strict',
		},
		storage: 'localStorage',
	},
	pwa: {
		registerType: 'autoUpdate',
		includeAssets: ['favicon.ico'],
		client: {
			installPrompt: true,
		},
		manifest: {
			name: 'TaskWith',
			description: '毎日を、あなたと一緒に',
			theme_color: '#4ca5cf',
			lang: 'ja',
			short_name: 'TaskWith',
			display: 'standalone',
			background_color: '#ffffff',
			icons: [
				{
					src: 'icons/icon-588x512.png',
					sizes: '512x512',
					type: 'image/png',
				},
			],
		},
		workbox: {
			navigateFallback: null,
		},
		devOptions: {
			enabled: false,
			type: 'module',
		},
	}
});
