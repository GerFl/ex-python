SELECT
    mdaMtr.claNodo,
    (mdaMtr.pml * tc.valor) AS precio
FROM (
    SELECT
        mda.claNodo,
        mda.fecha,
        mda.pml
    FROM MemSch.MemTraMDADet mda
    WHERE mda.claNodo = "01ANS-85"

    UNION ALL

    SELECT
        mtr.claNodo,
        mtr.fecha,
        mtr.pml
    FROM MemSch.MemTraMTRDet mtr
    WHERE mtr.claNodo = "01ANS-85"
) AS mdaMtr
INNER JOIN MemSch.MemTraTcDet tc
    ON mdaMtr.fecha = tc.fecha;