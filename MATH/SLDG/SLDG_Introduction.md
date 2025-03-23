---
title: SLDG - Introduction
icon: file
order: 3
author: Krigo, Xiaofeng Cai
category:
  - MATH
tags:
  - Research
footer: 
copyright: 
date: 2024-12-29
---

# Introduction

Semi-Lagrangian (SL) discontinuous Galerkin (DG) methods are a class of high-order deterministic transport solvers that enjoy advantages of both the SL approach and the DG spatial discretization.

- high-order
- deterministic transport solvers: 这个是指使用确定的数值方法 (deterministric numerical methods) 来求解传输方程 (transprot equations), 而非是 随机 / 蒙特卡洛方法。
    - Transport equations : 描述气体，能量，或信息在空间尺度和时间上的传输
- [The advantages of SL approach](https://www.notion.so/SLDG-Introduction-16d5c76b4e694853b1f419b149117f82?pvs=21)
- [The advantages of DG spatial discretization](https://www.notion.so/SLDG-Introduction-16d5c76b4e694853b1f419b149117f82?pvs=21)

<aside>
📐

首先我们需要注意，SLDG 是 “a class”, 一组 transport equations 的 numerical solver。

</aside>

## Discontinuous Galerkin (DG) Method

The DG methods belong to the family of finite element methods, which employ piecewise polynomials as approximation and test function spaces.

- For the time-dependent transport simulations, the DG methods are often coupled with the method-of-lines Eulerian framework, using appropriate time integrators for time evolution, e.g., the well-known TVD Runge-Kutta (RK) methods.
- It is well known that the DG method, when coupled with an explicit time integrator, suffers a very stringent CFL time step restriction for stability, which may be much smaller than that needed to resolve interesting timescales in physics.
- Implicit methods can be used to avoid the CFL time step restriction, yet the additional computational cost is required for solving the resulting linear or nonlinear system.

<aside>
📐

简单的说就是，DG 方法是FEM家族中的一个，经常在与时间有关的 transport simulation中，基于 Eulerian framework，通过使用合适的时间积分器进行演化。因为这里的 “合适的时间积分器”，在一些设计稳定性的时候，CFL设置的很严格。这样就导致一个问题：比如说，在对实际的物理问题中，我们需要稳定10s，但是因为CFL的设置，我们可能永远模拟不到第二秒。

- Eulerian framework
- 合适的时间积分器：符合某种CFL的积分方法？
- CFL:

DG 特点总结来说就是:

1. High-Order Accuracy
2. Local Conservation
3. Flexibility with Unstructured Meshes
4. Parallel Computation Friendly
5. Ability to Handle Discontinuities
</aside>

## Semi-Lagrangian (SL) Approach

- The SL approach allows for large time step evolution by incorporating the characteristic tracing mechanism without implicit treatments.
    - To alleviate the CFL time step restriction associated with the explicit Eulerian DG methods, the SLDG methods were developed in various settings.
- Meanwhile, the high-order accuracy can be conveniently attained because of its meshed-based nature.
- Note that the SL framework is flexible and hence able to accommodate various existing spatial discretization methods, see the [review paper](https://www.sciencedirect.com/science/article/abs/pii/S1570865916300023) .

<aside>
📐

简单的说，为了解决DG方法无法长时间进行simulation的问题，我们引入了SL方法。这个方法的优点就在于：[Large Time Step](https://www.notion.so/SLDG-Introduction-16d5c76b4e694853b1f419b149117f82?pvs=21)。通过这个优点来避免 CFL 的限制。

- 但是文章中还提到，这样构建的SLDG方法，还有 high order accuracy 的优点。我不太清楚这个优点究竟是怎么来的？

SL 的特点总结来说就是:

1. High order accuracy               - 高阶精度
2. Large Time Step                        - 大时间步长 (不需要严格的 CFL， 但是还是需要一个 CFL的，毕竟要满足框架嘛)
3. Small Numerical Dissipation - 低数值耗散
4. Ability to Handle Complex Structures - SL方法在处理如尖峰，不连续性时表现出色
</aside>

## Semi-Lagrangian Discontinuous Galerkin (SLDG) Method

- To alleviate the CFL time step restriction associated with the explicit Eulerian DG methods, the SLDG methods were developed in various settings.
- This kind of methods enjoys extraordinary computational advantages for transport simulations, such as
    - high-order accuracy,
    - provable unconditional stability and convergence,
    - local mass conservation,
    - small numerical dissipation,
    - superior ability to resolve complex solution structures.

### One-dimensional (1D) Transport problem

- There exist two types of SLDG methods: the characteristic Galerkin weak formulation and the flux difference formulation.

### Multi-diemsional Transprot problem

- The available SLDG methods can be classified into two categories depending on whether the operator splitting strategy is used.
    - The splitting based SL methods are popular in practice since one can directly make use of a preferred 1D SL formulation.
        - A celebrated example is the Strang splitting SL method for the Vlasov-Poisson (VP) system proposed by [Cheng and Knorr](https://www.sciencedirect.com/science/article/pii/002199917690053X)
    - In particular, the nonlinearly coupled highdimensional transport equation is decomposed into a set of lower dimensional sub-equations that are linear and hence much easier to evolve numerically in the SL setting.
        - Following a similar idea, many splitting SL schemes based on various spatial discretization are designed, such as [finite volume-based](https://www.sciencedirect.com/science/article/pii/S0021999101968184) and [finite difference-based](https://www.sciencedirect.com/science/article/pii/S0021999116303163) methods.
        - 这里提到了一个 “sub-equations”，这个的意思需要明确一下
    - On the other hand, the splitting methods suffer from the inherent splitting error.
        - For instance, if the Strang splitting is used, then the second-order splitting error in time is incurred.
            - As mentioned in [13], such a relatively low-order error may become significant for long-term transport simulations and hence greatly compromise the performance of the SL methods.
    - In addition, for some nonlinear problems, it can be very difficult to track characteristics accurately for the split subequations, posing challenges for the development of high-order splitting SL methods.
- To completely avoid the splitting error, several non-splitting SL methods are developed.
    - The first non-splitting SLDG scheme is proposed with [A semi-Lagrangian discontinuous Galerkin method for scalar advection by incompressible flows](https://www.sciencedirect.com/science/article/pii/S0021999105005486)
        - Such a method is based on a flux difference form but subject to a CFL time step restriction, degrading its computational efficiency to some extent.
        - Recently, a line of research has been carried out for the development of non-splitting SLDG methods （老蔡的3篇文章 + [一篇LLNL的](https://www.sciencedirect.com/science/article/pii/S0021999116303539)）
            - The proposed methods are unconditionally stable, leading to computational efficiency.
            - Meanwhile, the implementation is much more involved than the splitting counterpart, especially for problems in higher dimensions

<aside>
📐

建议这部分直接看我整理的原文，重点已经拿红色标注了。我简单总结一下，这些solver的特点总结来说就是:

1. 
</aside>