import { configureStore, combineReducers } from "@reduxjs/toolkit";
import { PersistConfig, persistReducer, persistStore, REHYDRATE, FLUSH, PERSIST, PURGE, PAUSE } from "redux-persist"
import storage from "redux-persist/lib/storage"


import { authApi } from "../service/authApi";
import { setupListeners } from "@reduxjs/toolkit/query/react";
import authReducer from "../features/authSlice";
import jobReducer from "../features/jobSlice";
import taskReducer from "../features/taskSlice";
import { jobApi } from "../service/jobApi";
import { taskApi } from "../service/taskApi";


const config : PersistConfig<any> = {
  key: "root",
  storage,
  blacklist: [jobApi.reducerPath,taskApi.reducerPath]
}

const reducer = combineReducers({
  auth:authReducer,
  job:jobReducer,
  task:taskReducer,
 [authApi.reducerPath]: authApi.reducer,
 [jobApi.reducerPath]: jobApi.reducer,
 [taskApi.reducerPath]:taskApi.reducer,
 })

const peristedReducer = persistReducer(config, reducer)

export const store = configureStore({
    reducer: peristedReducer,
    middleware: (getDefaultMiddleware) => {
        return getDefaultMiddleware({
          serializableCheck: false
        }).concat(authApi.middleware).concat(jobApi.middleware).concat(taskApi.middleware);
      },
})



export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
setupListeners(store.dispatch)

export const persistor = persistStore(store)