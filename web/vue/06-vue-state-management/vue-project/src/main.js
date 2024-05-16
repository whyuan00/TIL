import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
<<<<<<< HEAD
import { createApp } from 'vue'
import { PiniaVuePlugin, createPinia } from 'pinia'

=======

import { createApp } from 'vue'
import { createPinia } from 'pinia'
>>>>>>> 0db8f7e851a046df1112dd11b4859c48df8d7aac
import App from './App.vue'

const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)

// app.use(createPinia())
app.use(pinia)

app.mount('#app')
