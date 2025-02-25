SELECT
    mdaMtr.claNodo,
    mdaMtr.fecha,
    mdaMtr.hora,
    mdaMtr.pml,
    tc.valor,
    tb.TbFin
FROM (
    SELECT
        mda.claNodo,
        mda.fecha,
        mda.hora,
        mda.pml
    FROM MemSch.MemTraMDADet mda

    UNION ALL

    SELECT
        mtr.claNodo,
        mtr.fecha,
        mtr.hora,
        mtr.pml
    FROM MemSch.MemTraMTRDet mtr
) AS mdaMtr
INNER JOIN MemSch.MemTraTcDet tc
    ON mdaMtr.fecha = tc.fecha
INNER JOIN MemSch.MemTraTBFinVw tb
    ON mdaMtr.fecha = tb.fecha;