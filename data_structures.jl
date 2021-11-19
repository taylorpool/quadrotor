module data_structures
    struct QuadrotorState
        p::AbstractVector
        v::AbstractVector
        R::AbstractMatrix
        omega::AbstractVector
    end

    struct QuadrotorStateDerivative
        pDot::AbstractVector
        vDot::AbstractVector
        RDot::AbstractMatrix
        omegaDot::AbstractVector
    end
end