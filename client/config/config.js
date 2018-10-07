export default {
    routes: [{
        path: "/",
        component: "../layout",
        routes: [
            {
                path: '/',
                component: './HelloWorld'
            },
            {
                path: "/helloworld",
                component: "./HelloWorld"
            },
            {
                path: '/dashboard',
                routes: [
                    {path: '/dashboard/analysis', component: 'Dashboard/Analysis'},
                    {path: '/dashboard/monitor', component: 'Dashboard/Monitor'},
                    {path: '/dashboard/workplace', component: 'Dashboard/Workplace'},
                ]
            },
            {
                path: '/puzzlecards',
                component: './puzzlecards'
            }
        ]
    }],
    singular: true,
    plugins: [
        ['umi-plugin-react', {
            antd: true,
            dva: true,
        }],
    ],
    proxy: {
        "/user": {
            target: 'http://127.0.0.1:5000/',
            changeOrigin: true,
        }
    }
};
