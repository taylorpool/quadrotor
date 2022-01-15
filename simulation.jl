using DifferentialEquations
using Plots
using Rotations
using LinearAlgebra

position = 1:3
velocity = 4:6
orientation = 7:10
angular_velocity = 11:13
wx = 11
wy = 12
wz = 13

function rigid!(du, u, p, t)
    F = p.F(u[position])
    T = p.T(u[position])
    du[position] = u[velocity]
    du[velocity] = F/p.m
    du[orientation] = 0.5*[
        0.0 -u[wx] -u[wy] -u[wz]
        u[wx] 0.0 u[wz] -u[wy]
        u[wy] -u[wz] 0.0 u[wx]
        u[wz] u[wy] -u[wx] 0.0
    ]*u[orientation]
    du[angular_velocity] = p.J\(T - cross(u[angular_velocity], p.J*u[angular_velocity]))
end

struct BodyParams
    F
    T
    m
    J
end

params = BodyParams(-, -, 10.0, I)

state0 = [
    1.0 # px
    0.0 # py
    0.0 # pz
    0.0 # vx
    1.0 # vy
    0.5 # vz
    1.0 # q1
    0.0 # q2
    0.0 # q3
    0.0 # q4
    0.0 # w1
    0.0 # w2
    0.0 # w3
]
tspan = (0.0, 100.0)
prob = ODEProblem(rigid!, state0, tspan, params)
sol = solve(prob)