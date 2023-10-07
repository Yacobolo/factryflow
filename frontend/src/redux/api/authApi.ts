import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import customFetchBase from "./customeFetchBase";
import {
  Login,
  Register,
  LoginResponse,
  RegisterResponse,
  GenericResponse,
} from "@/types/api.types";

export const authApi = createApi({
  reducerPath: "authApi",
  baseQuery: customFetchBase,
  endpoints: (builder) => ({
    loginUser: builder.mutation<GenericResponse<LoginResponse>, Login>({
      query: (body) => {
        return {
          url: "api/token/pair",
          method: "post",
          body,
        };
      },
    }),
    registerUser: builder.mutation<GenericResponse<RegisterResponse>, Register>(
      {
        query: (body: {
          first_name: string;
          last_name: string;
          email: string;
          password: string;
        }) => {
          return {
            url: "api/users",
            method: "post",
            body,
          };
        },
      }
    ),
    changePassword: builder.mutation({
      query: (body) => {
        return {
          url: "api/change-password/",
          method: "put",
          body,
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        };
      },
    }),
    getProfile: builder.query({
      query: () => {
        return {
          url: `api/user-details/`,
          method: "get",
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        };
      },
    }),
  }),
});

export const {
  useLoginUserMutation,
  useRegisterUserMutation,
  useChangePasswordMutation,
  useGetProfileQuery,
} = authApi;
export default authApi;