SELECT
    mdaMtr.claNodo,
    mdaMtr.fecha,
    mdaMtr.hora,
    mdaMtr.pml
FROM (
    SELECT
        mda.claNodo,
        mda.fecha,
        mda.hora,
        mda.pml
    FROM MemSch.MemTraMDADet mda
    WHERE mtr.claNodo = "01ANS-85"

    UNION ALL

    SELECT
        mtr.claNodo,
        mtr.fecha,
        mtr.hora,
        mtr.pml
    FROM MemSch.MemTraMTRDet mtr
    WHERE mtr.claNodo = "01ANS-85"
) AS mdaMtr
ORDER BY
    mdaMtr.claNodo ASC,
    mdaMtr.fecha DESC,
    mdaMtr.hora ASC;